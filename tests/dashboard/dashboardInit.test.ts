import { test } from '../../src/utils/fixtures'; // Import the custom test object
import { DashboardPage } from "../../src/pages/dashboard/DashboardPage";

test('Validate dashboard access after login', async ({ page }) => {
  let dashboardPage = new DashboardPage(page);

  await dashboardPage.openPage();
});
