#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list.
 *
 * Return: 0 if no cycle, 1 if there's a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	listint_t *current;

	current = list;
	temp = current;

	while (current != NULL)
	{
		current = current->next;
		if (current == temp)
			return (1);
	}

	return (0);
}
