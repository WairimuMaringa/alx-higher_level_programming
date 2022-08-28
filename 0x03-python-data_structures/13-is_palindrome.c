#include "lists.h"
#include <stdio.h>

/**
 * comparator - compares the start and end positions
 * @head: head of linked list
 * @end: end of linked list
 * Return: 1 if true, 0 if false
 */
int comparator(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (comparator(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a singlylinkedlist is a palindrome
 * @head: head of linked list
 * Return: 1 if true, 0 if false
 */

int is_palindrome(listint_t **head)
{
	if (!head || !(*head))
		return (1);
	return (comparator(head, *head));
}
