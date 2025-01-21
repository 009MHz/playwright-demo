# Playwright TypeScript Project Documentation
## Folder Breakdown

### `.github/workflows/`
- **playwright.yml**: Contains GitHub Actions workflow for CI/CD.

### `elements/`
Defines reusable selectors for pages.
- **login/LoginElements.ts**: Selectors for login-related elements.
- **dashbord/**: Selectors for various user roles:
  - Guest, Common, Premium, Admin.

### `pages/`
Encapsulates page-specific actions and interactions.
- **login/LoginPage.ts**: Actions for login operations.
- **dashbord/**: Actions for user roles:
  - GuestUser, Premium, Admin, CommonUser.

### `utils/`
Utility files for browser configuration and session handling.
- **browserConfig.ts**: Configures browser settings.
- **fixtures.ts**: Shared test fixtures.
- **sessionStarter.ts**: Handles session initialization.
- **GlobalTeardown.ts**: Teardown operations post-tests.
- **SessionHandler.ts**: Manages session tokens.
- **UrlRouting.ts**: Handles application URL routing.

### `tests/`
Contains test scripts.
- **login/**: Tests for login functionality:
  - Valid and invalid login scenarios.
- **dashbord/**: Tests for various user roles:
  - Smoke tests for guest users.
  - Functional tests for premium and admin users.

### Root Files
- **playwright.config.ts**: Playwright configuration.
- **tsconfig.json**: TypeScript configuration.
- **package.json**: Project metadata and dependencies.
- **README.md**: Project documentation.

## CI/CD
## GitHub Actions Workflow
The `.github/workflows/playwright.yml` handles CI/CD for running Playwright tests on different browsers and configurations. It integrates Allure for reporting test results.

## Reporting
- **Allure Reporter**: Configured in `playwright.config.ts` with:
  - Results directory: `reports`
  - Suite titles and detail level customization.

## Command Line Options

## Running Tests with/without Report
- Without Allure report:
  ```bash
  npx playwright test --reporter=list
  ```
- With Allure report:
  ```bash
  npx playwright test --reporter=allure-playwright
  ```

## Running Tests with/without Attachments
- Without attachments:
  ```bash
  npx playwright test --trace=off --screenshot=off --video=off
  ```
- With attachments:
  ```bash
  npx playwright test --trace=on-first-retry --screenshot=on --video=on
  ```

## Running Tests on Specific Browser
- Chromium:
  ```bash
  npx playwright test --project=chromium
  ```
- Firefox:
  ```bash
  npx playwright test --project=firefox
  ```
- Webkit:
  ```bash
  npx playwright test --project=webkit
  ```

## Running Tests on Specific Test Suites
- Specify a suite by file path:
  ```bash
  npx playwright test tests/login/login.test.ts
  ```

## Running Tests on Specific Features Only
- Use a tag to filter tests:
  ```bash
  npx playwright test --grep @featureTag
  ```
- Exclude specific features:
  ```bash
  npx playwright test --grep-invert @excludedFeatureTag
  ```

## Running Tests Using Specific Worker
- Limit to a specific worker:
  ```bash
  npx playwright test --workers=1
  ```

## Scripts
Install dependencies and run tests:
1. Install dependencies:
   ```bash
   npm install
   ```
2. Run tests:
   ```bash
   npx playwright test
   ```
3. Generate Allure reports:
   ```bash
   allure generate reports && allure open
   ```

## Notes
- Ensure Allure Command Line is installed for generating reports.
- Test results include screenshots and traces for debugging.

