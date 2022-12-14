#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include "lists.h"
#include <string.h>
/**
 * insert_node - insert number into a sorted singleylinked list
 * @head: head
 * @number: value to be inserted
 * Return: list with added value
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp_head, *prev_node;

	tmp_head = *head;
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!(*head) || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	while (tmp_head)
	{
		if (tmp_head->n > number)
		{
			break;
		}
		prev_node = tmp_head;
		tmp_head = tmp_head->next;
	}
	new_node->next = tmp_head;
	prev_node->next = new_node;
	return (*head);
}
