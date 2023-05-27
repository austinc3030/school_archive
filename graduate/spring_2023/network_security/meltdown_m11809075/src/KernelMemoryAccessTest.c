int main()
{
    char *kernel_data_addr = (char*)0x49f9dadb;
    char kernel_data = *kernel_data_addr;
    printf("I have reached here.\n");
    return 0;
}