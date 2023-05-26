#include "lists.h"

/**
 * check_cycle - use two pointers (hare and tortoise) to check for a cycle in a linked list
 * @list: a linked list to traverse
 * Return - (1) on success and (0) on failure to find a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	if (list == NULL || list->next == NULL)
		return 0;

	tortoise = list;
	hare = list->next;

	while (tortoise != NULL && hare != NULL && hare->next != NULL)
	{
		if (tortoise == hare)
			return (1);
		hare = hare->next->next;
		tortoise = tortoise->next;
	}

	return 0;
}