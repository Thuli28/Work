#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    int binary[BITS_IN_BYTE];
    int decimal_value;
    string input = get_string("Message: ");
    int length = strlen(input);
    for (int i = 0; i < length; i++)
    {
        decimal_value = input[i];
        for (int a = BITS_IN_BYTE - 1; a > 0; a--)
        {
            binary[a] = decimal_value % 2;
            decimal_value /= 2;
        }
        for (int a = 0; a < BITS_IN_BYTE; a++)
        {
            print_bulb(binary[a]);
        }
        printf("\n");

    }



}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
