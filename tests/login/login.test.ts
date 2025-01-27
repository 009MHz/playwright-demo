import * as allure from "allure-js-commons";
import { test } from "@utils/fixtures"; // Use the custom test with fixtures
import { LoginPage } from "@pages/login/LoginPage";

export const features = (featureList?: string | string[]) => {
  if (featureList) {
    const features = Array.isArray(featureList) ? featureList : [featureList];
    features.forEach((feature) => allure.feature(feature));
  }
};

test.describe("Login Page - Unit Test (Guest Mode)", () => {
  let logIn: LoginPage;

  test.beforeEach(async ({ guestPage }) => {
    logIn = new LoginPage(guestPage.page); // Use the guestPage fixture
    allure.epic("Login");
    allure.story("Login Page Unit Test");
    await logIn.openPage();
  });

  test("Login Page Initial State Check: Page Header & Information", async () => {
    allure.severity("Medium");
    features([
      "Login Page/ Header",
      "Login Page/ Subheader",
    ]);

    await allure.step("Verify the header existence", async () => 
      logIn.PageInfoPresence()
    );

    await allure.step("Verify the credentials hints existence", async () => 
      logIn.PageHintsPresence()
    );
  });

  test("Login Page Initial State Check: Login Form Component", async () => {
    allure.severity("Critical");
    features([
      "Login Page/ Login Form",
      "Login Page/ Login Form/ Username",
      "Login Page/ Login Form/ Password",
      "Login Page/ Login Form/ Login Button",
    ]);

    await allure.step('Verify the "username" field', async () =>
      logIn.usernameInputPresence()
    );

    await allure.step('Verify the "password" field', async () =>
      logIn.passwordInputPresence()
    );

    await allure.step('Verify the "Login" button', async () =>
      logIn.LoginButtonPresence()
    );
  });

  test("Normal Login Page Action Flow", async () => {
    allure.severity("Critical");
    features([
      "Login Page/ Login Form",
      "Login Page/ Login Form/ Username",
      "Login Page/ Login Form/ Password",
      "Login Page/ Login Form/ Login Button",
    ]);

    await allure.step("Insert a valid username", async () =>
      logIn.usernameInsert("Admin")
    );

    await allure.step("Insert a valid password", async () =>
      logIn.passwordInsert("admin123")
    );

    await allure.step('Click on the "Login" button', async () =>
      logIn.clickLoginBtn()
    );
  });
});
