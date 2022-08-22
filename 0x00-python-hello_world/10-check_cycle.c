#include "lists.h"

/**
check_cycle - singly linked list with a cycle
@list: structure
Return: 0 if no cycle, otherwise 1
*/

int check_cycle(listint_t *list)
{
listint_t *l_fast, *l_slow;
l_fast = l_slow = list;

if (list == NULL)
return (0);

while (l_slow && l_slow->next && l_slow->next->next)
{
l_fast = l_fast->next;
l_slow = l_slow->next->next;

if (l_fast == l_slow)
return (1);
}
return (0);
}
