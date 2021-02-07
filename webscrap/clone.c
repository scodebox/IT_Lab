#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Function to fetch the webpage and store into a file.
void fetchweb()
{
    printf("\n\n\t FETCHING THE WEB PAGE... \n\n");
    // Using curl command to clone the web page.
    system("curl http://127.0.0.1:8080/ > raw_text.txt");
    // system("curl http://10.254.254.38/0/up/ > raw_text.txt");
    printf("\n\n\t FETCHED.\n");
}

// Function to remove HTML tags from the file.
int normalize()
{
    // Input file and output file.
    FILE *fp;
    FILE *out_file;
    fp = fopen("raw_text.txt", "r");
    out_file = fopen("normalized.txt", "w");

    if (NULL == fp || NULL == out_file)
    {
        printf("not found");
        return -1;
    }
    else
    {
        printf("REMOVING HTML TAGS\n");

        int flag, space = 0, line = 0, line_count = 1;
        char c = getc(fp);
        // Printing the line number.
        fprintf(out_file, "%d ", line_count++);

        while (c != EOF)
        {
            // Reseting flag for not to write in file.
            if (c == '<')
                flag = 0;
            // Write when flag is set and input char is alphabet or digit.
            if (flag && (isalpha(c) || isdigit(c)))
            {
                // putchar(c);
                fprintf(out_file, "%c", c);
                space = 1;
                line = 1;
            }
            else
            {
                // Write only one space and discard all duplicate space.
                if (c == ' ' && space)
                {
                    // putchar(c);
                    fprintf(out_file, "%c", c);
                    space = 0;
                }
                // Write only one new line and discard all duplicate new line.
                if (c == '\n' && line)
                {
                    // putchar(c);
                    fprintf(out_file, "%c", c);
                    fprintf(out_file, "%d ", line_count++);
                    line = 0;
                    space = 0;
                }
            }
            // Setting for write in file.
            if (c == '>')
                flag = 1;
            c = getc(fp);
        }
    }

    // Cloding files.
    fclose(fp);
    fclose(out_file);
    printf("DONE!\n");

    return 1;
}

// Function to extract unique words from each line.
int extract_unique()
{
    // Input and output file.
    FILE *fp;
    FILE *unique_file;
    fp = fopen("normalized.txt", "r");
    unique_file = fopen("unique.txt", "w");
    if (NULL == fp || NULL == unique_file)
        return -1;

    // To store word list of each line.
    char word[100];
    char word_list[1000][100];
    int list_index = 0;
    int line_number = 1;

    // To keep track of duplicate words.
    int duplicate_counter[1000];
    for (int i = 0; i < 1000; i++)
        duplicate_counter[i] = 0;

    // Reading the first line number.
    fscanf(fp, "%s", word);
    printf("EXTRACTING UNIQUE WORDS!\n");
    while (fscanf(fp, "%s", word) != EOF)
    {
        // If new line.
        if (isdigit(word[0]))
        {
            // Write the previous line.
            for (int i = 0; i < list_index; i++)
                fprintf(unique_file, "line no: %d, sequence no: %d, word: '%s', count: %d\n", line_number, i, word_list[i], duplicate_counter[i]);

            // Count line
            line_number++;
            // reinitialize
            for (int i = 0; i < 1000; i++)
                duplicate_counter[i] = 0;
            list_index = 0;
        }
        else
        {
            // Flag and index variables.
            int unique = 1;
            int i;
            // Checking if the string is duplicate.
            for (i = 0; i < list_index && unique; i++)
            {
                if (strcmp(word_list[i], word) == 0)
                {
                    unique = 0;
                }
            }
            // If not duplicate add the word in list.
            if (unique)
            {
                strcpy(word_list[list_index], word);
                duplicate_counter[list_index]++;
                list_index++;
            }
            // If duplicate then just count it.
            else
                duplicate_counter[i - 1]++;
        }
    }

    // close files.
    fclose(fp);
    fclose(unique_file);
    printf("DONE!\n");

    return 1;
}

int main()
{
    // Fetch the web page.
    fetchweb();
    // Remove HTML tags.
    normalize();
    // Extract unique words and write back details into a file.
    extract_unique();

    return 0;
}