#include <iostream>
#include "shop.h"
#include "menu.h"

// Driver file - main function
int main()
{
	Shop test_shop;

	test_shop.load_data();

	test_shop.view_shop_detail();

	Menu m1(10);
	Menu m2(5);

	return 0;
}