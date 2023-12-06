// Test enum
#include <stdio.h>

typedef enum {
    POS = 0,
    NEG,
} Eval;

struct TestEnum {
    Eval eval;
};

void setEval(struct TestEnum *news, Eval e)
{
    news->eval = e;
}

int main(void)
{
    struct TestEnum enum1;
    setEval(&enum1, NEG);
    printf("%d\n", enum1.eval);
    return 0;
}

