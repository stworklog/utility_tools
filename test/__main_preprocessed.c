# 0 "main.c"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 0 "<command-line>" 2
# 1 "main.c"
# 1 "mid_layer_1.h" 1



# 1 "types.h" 1



struct foobar {
 int a;
 int b;
 float f;
};
# 5 "mid_layer_1.h" 2
# 2 "main.c" 2
# 1 "mid_layer_2.h" 1
# 3 "main.c" 2

int main(void)
{
    struct foobar m;
    m.a = 1;
    m.b = 2;
    m.f = 3.0;

    return 0;
}
