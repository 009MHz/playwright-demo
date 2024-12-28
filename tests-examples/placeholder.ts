// Single Allure Test approach
// test('Testing Step', async () => {
//   await allure.step('1. Testing Step a', async() =>
//     module.children1());  

//   await allure.step('2. Testing Step b', async() =>
//     module.children2());  

//   await allure.step('3. Testing Step c', async() =>
//     module.children3));  
// });



// Parametrized Allure Test approach
// for (const { scheme, username } of [
//   { scheme: "incorrect", username: "InvalidUser" },
//   { scheme: "empty", username: "" },
// ]) {
//   test(`'${scheme}' username scenario, should return the correct information`, async ({ page }) => {
//     allure.severity("Medium");
//     allure.description(`Scenario: \`${scheme}\``);

//     await allure.step(`1. Insert \`${scheme}\` value on the username field`, async () => {
//       await logIn.usernameInsert(username);
//     });

//     await allure.step('2. Insert a valid password', async () => {
//       await logIn.passwordInsert('SuperSecretPassword!');
//     });

//     await allure.step('3. Click on the Login button', async () => {
//       await logIn.clickLoginBtn();
//     });

//     await allure.step(`4. Verify the ${scheme} banner presence`, async () => {
//       await logIn.invalidBannerUsernamePresence();
//     });
//   });
// }