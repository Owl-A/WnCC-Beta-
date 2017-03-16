#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    int occur = 0;
    int itr = 2;
    char * testStr = argv[itr];
    char * target = argv[1];
    while ((*testStr != '\0') && (itr >= argc))
    {
        for(char * inTestStr = testStr ; ((*target == *inTestStr) || (*target == '\0')) ; target++,inTestStr++)
        {
            if(*target == '\0')
            {
                occur++;
                target = argv[1];
                testStr = inTestStr;
                continue;
            }
        }
        target = argv[1];
        testStr++;
    }
    return occur;
}