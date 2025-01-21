export class PageInfo {
  static url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index";
  static navbarTop = ".oxd-topbar-header"
  static leftSidebar = ".oxd-sidepanel-body";
  static pageFooter = ".oxd-sidepanel-body";
}

export class Navbar{
  static breadCrumb = "//span[contains(@class, 'breadcrumb')]";
  static btnUpgrade = ".oxd-glass-button.orangehrm-upgrade-button";
  static userAvatar = {
    userImage: "img[alt='profile picture']",
    userName: ".oxd-userdropdown-name",
    dropDown: {
      button: ".oxd-icon.bi-caret-down-fill.oxd-userdropdown-icon",
      panel: "ul[class='oxd-dropdown-menu']",
      aboutCta: "text='About'",
      supportCta: "//a[contains(@href, 'support')]",
      changePassCta: "//a[contains(@href, 'updatePassword')]",
      logoutCta: "//a[contains(@href, 'logout')]"
    }
  }
}

export class LeftPanel {
  static hideToggle = ".oxd-icon-button oxd-main-menu-button";
  static images = ".oxd-brand-banner";
  static search = "//input[contains(@class, 'input')]"
  static admin = "//a[contains(@href, 'Admin')]";
  static PIM = "//a[contains(@href, 'Pim')]";
  static leave = "//a[contains(@href, 'Leave')]";
  static time = "//a[contains(@href, 'Time')]";

}
