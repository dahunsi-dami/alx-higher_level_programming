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
	listint_t *temp, *current;

	temp = current = list;

	while (temp && current && temp->next != NULL)
	{
		current = current->next;
		temp = temp->next->next;
		if (current == temp)
			return (1);
	}

	return (0);
}
