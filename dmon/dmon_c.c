#include "dmon_c.h"

// data files
char fn[100]; 
FILE *fp[N+1];

int fds[N+1][2]; // pipe communication b/w agents

/* 
Agent i checks and receives right root events from other agents,
then add event info into the local buffer.
*/
int recv_root(Agent i, ListNode *head) {
    fd_set read_fd;
    int ret;
    struct timeval timeout = {0, 500};
    
    FD_ZERO(&read_fd);
    FD_SET(fds[i][0], &read_fd);
    
    // Monitor pipe if it has data to be read
    ret = select(fds[i][0]+1, &read_fd, NULL, NULL, &timeout);

    if (ret > 0) {
        Event e_m;
        memset(&e_m, 0, sizeof(Event));
        read(fds[i][0], &e_m, sizeof(Event));
        printf("message arrived from %d to %d\n", e_m.agent, i);
        append(&head, e_m);
    }
    return 0;
}


int main(int argc, char *argv[]) {
    for (int j = 1; j <= N; j++) {
        pipe(fds[j]);
    }
    for (Agent i = 1; i <= N; i++) {
        if (fork() == 0) {  // child process - agent
            
            // Local buffer
            ListNode *loc_buf_head = NULL;
            
            // Read file
            sprintf(fn, "../signals/signal%d.txt", i);
            fp[i] = fopen(fn, "rt");
            char line[255];
            char *p;
            fgets(line, sizeof(line), fp[i]);   // discard the first line

            double prev_x = -INFINITY, cur_x = -INFINITY;
            Time prev_t = 0, cur_t = 0;
            
            unsigned int pc = 0;    // imaginary counter, not global clock
            while (pc++ < 50) {
                if (!feof(fp[i])) {
                    // get t and x(t) from each line
                    fgets(line, sizeof(line), fp[i]);
                    // printf("%s", line);
                    p = strtok(line, ",");
                    cur_t = atof(p);
                    p = strtok(NULL, ",");
                    cur_x = atof(p);
                    // printf("t = %.2f, x(t) = %.2f\n", cur_t, cur_x);
                    // TODO: handle multiple 0s and interpolate time
                 
                }
            
                // Abstractor - 1. Detect roots
                if ((prev_x < 0 && cur_x > 0) || (prev_x > 0 && cur_x < 0)) {
                    // Determine left or right root
                    RootType type = prev_x < 0 ? LEFT : RIGHT;
                    
                    // Create an event, then add to the local buffer
                    Time pvc[N];
                    memset(pvc, 0, sizeof(Time) * N);
                    Time root_loc = (prev_t * cur_x - cur_t * prev_x) / (cur_x - prev_x);
                    pvc[i-1] = root_loc;
                    Event e = {i, root_loc, pvc, type};
                    append(&loc_buf_head, e);
                    
                    // Right foot, then broadcast
                    if (type == RIGHT) {
                        for (Agent l = 1; l <= N; l++) {
                            if (l != i) {
                                write(fds[l][1], &e, sizeof(Event));
                                printf("writing from %d to %d\n", i, l);
                            }
                        }
                    }
                }

                // Abstractor - 2. Receive right roots from other agents
                recv_root(i, loc_buf_head);
                // call solver

                if (cur_x != 0) {
                    prev_t = cur_t;
                    prev_x = cur_x;
                }
            }
            printf("Agent %d loc buffer\n", i);
            print_list(loc_buf_head);
            exit(0);
        } // end of child process
       
    }

    while(wait(NULL) > 0);  // wait for all child processes

}

