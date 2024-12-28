import * as allure from "allure-js-commons";
import { test } from "@playwright/test";
import { LoginPage } from "../../pages/login/loginPage";
import { PreCond } from "../../pages/login/PreCond";

export const features = (
  featureList?: string | string[]
) => {
  if (features) {
    const featureList = Array.isArray(features) ? features : [features];
    featureList.forEach(feature => allure.feature(feature));
  }
};

test.describe("Login Page - Unit Test", () => {
  let logIn: LoginPage;
  let preCond: PreCond;

  test.beforeEach(async ({ page }) => {
    preCond = new PreCond(page);
    logIn = new LoginPage(page);
    allure.epic("Login")
    allure.story("Login Page Unit Test")
    await preCond.loadLoginPage();
  });

  test("Login Page Initial State Check: Page Header & Information", async () => {
    allure.severity("Medium")
    features([
      "Login Page/ Header",
      "Login Page/ Subheader"
    ]);

    await allure.step("Verify the header existence", async () =>
      logIn.HeaderPresence()
    );

    await allure.step("Verify the subheader presence", async () =>
      logIn.SubheaderPresence()
    );
  });

  test("Login Page Initial State Check: Login Form Component", async () => {
    allure.severity("Critical")
    features([
      "Login Page/ Login Form",
      "Login Page/ Login Form/ Username",
      "Login Page/ Login Form/ Password",
      "Login Page/ Login Form/ Login Button"
    ]);

    await allure.step('Verify the "username" field', async () =>
      logIn.usernameFieldPresence()
    );

    await allure.step('Verify the "password" field', async () =>
      logIn.passwordFieldPresence()
    );

    await allure.step('Verify the "Login" button', async () =>
      logIn.loginButtonPresence()
    );
  });

  test("Normal Login Page Action Flow", async () => {
    allure.severity("Critical")
    features([
      "Login Page/ Login Form",
      "Login Page/ Login Form/ Username",
      "Login Page/ Login Form/ Password",
      "Login Page/ Login Form/ Login Button"
    ]);

    await allure.step("Insert a valid username", async () =>
      logIn.usernameInsert("tomsmith")
    );

    await allure.step("Insert a valid password", async () =>
      logIn.passwordInsert("SuperSecretPassword!")
    );

    await allure.step('Click on the "Login" button', async () =>
      logIn.clickLoginBtn()
    );
  });

  const invalidUsernameScenarios = [
    { scheme: "incorrect", username: "InvalidUser" },
    { scheme: "empty", username: "" },
  ];

  invalidUsernameScenarios.forEach(({ scheme, username }) => {
    test(`Invalid Username: '${scheme}' scenario`, async () => {
      allure.severity("Medium")
      features([
        "Login Page/ Login Form",
        "Login Page/ Invalid Banner/",
        "Login Page/ Invalid Banner/ Invalid Username"
      ]);

      allure.description(`Scenario: \`${scheme}\``);

      await allure.step(`Insert \`${scheme}\` value on the username field`, async () =>
        logIn.usernameInsert(username)
      );

      await allure.step("Insert a valid password", async () =>
        logIn.passwordInsert("SuperSecretPassword!")
      );

      await allure.step("Click on the Login button", async () =>
        logIn.clickLoginBtn()
      );

      await allure.step(`Verify the ${scheme} banner presence`, async () =>
        logIn.invalidBannerUsernamePresence()
      );
    });
  });

  const invalidPasswordScenarios = [
    { scheme: "incorrect", password: "InvalidPassword" },
    { scheme: "empty", password: "" },
  ];

  invalidPasswordScenarios.forEach(({ scheme, password }) => {
    test(`Invalid Password: '${scheme}' scenario`, async () => {
      allure.severity("Medium")
      features([
        "Login Page/ Invalid Banner/",
        "Login Page/ Invalid Banner/ Invalid Password"
      ]);
      allure.description(`Scenario: \`${scheme}\``);

      await allure.step("Insert a valid user on the username field", async () =>
        logIn.usernameInsert("tomsmith")
      );

      await allure.step(`Insert \`${scheme}\` value on the password field`, async () =>
        logIn.passwordInsert(password)
      );

      await allure.step("Click on the Login button", async () =>
        logIn.clickLoginBtn()
      );

      await allure.step(`Verify the ${scheme} banner presence`, async () =>
        logIn.invalidBannerPasswordPresence()
      );
    });
  });
});
