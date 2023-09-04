#include "lists.h"

/**
 * check_cycle - check if list is cycle
 * 
 * @list: pointer to list to check
 *
 * Return: 1 if there cycle, 0 or not
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);

	}
	return (0);
}
