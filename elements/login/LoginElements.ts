export class PageInfo {
  static url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login";
  static brand = "img[alt='company-branding']"; // CSS selector for the branding image
  static title = "//h5[contains(@class, 'login-title')]"; // XPath for the login title
  static hintsWrapper = "//div[contains(@class, 'credentials')]"
  static hintsUser = "text='Username : Admin'"; // Text selector for username hint
  static hintsPassword = "text='Password : admin123'"; // Text selector for password hint
}

export class PageForm {
  static usernameLabel = "//label[contains(., 'Username')]"; // XPath text value RegEx for the username label
  static usernameInput = "input[name='username']"; // CSS selector for username input field
  static passLabel = "//label[contains(., 'Password')]"; // XPath text value RegEx for the password label
  static passInput = "input[name='password']"; // CSS selector for password input field
  static loginBtn = "//button[contains(@class, 'login-button')]"; // CSS selector for the login button
  static forgotPass = ".orangehrm-login-forgot";
}
