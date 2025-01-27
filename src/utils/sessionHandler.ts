import { Page, BrowserContext } from 'playwright';
import { LoginPage } from '@pages/login/LoginPage';
import fs from 'fs';
import path from 'path';

const SESSION_DIR = path.resolve('.auth');
const USER_SESSION_FILE = path.join(SESSION_DIR, 'session.json');
const SESSION_EXPIRATION_DURATION = 3600000; // 1 hour in milliseconds

export class AuthStarter {
  private page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  private static checkSessionDir() {
    if (!fs.existsSync(SESSION_DIR)) {
      fs.mkdirSync(SESSION_DIR, { recursive: true });
    }
  }

  private static isSessionExpired(): boolean {
    if (!fs.existsSync(USER_SESSION_FILE)) return true;

    const sessionStats = fs.statSync(USER_SESSION_FILE);
    const currentTime = Date.now();
    const lastModifiedTime = sessionStats.mtime.getTime();

    return currentTime - lastModifiedTime > SESSION_EXPIRATION_DURATION;
  }

  private async createSession() {
    const username = process.env.USERNAME || 'defaultUser';
    const password = process.env.PASSWORD || 'defaultPass';

    const loginPage = new LoginPage(this.page);
    await loginPage.LoginInit(username, password);
    await this.page.context().storageState({ path: USER_SESSION_FILE });
    console.log('Session created and saved.');
  }

  private async loadSession(context: BrowserContext) {
    if (!fs.existsSync(USER_SESSION_FILE)) {
      throw new Error(`Session file not found: ${USER_SESSION_FILE}`);
    }

    await context.addInitScript(storageState => {
      for (const [key, value] of Object.entries(storageState.cookies)) {
        window.document.cookie = `${key}=${value}`;
      }
    }, JSON.parse(fs.readFileSync(USER_SESSION_FILE, 'utf-8')));

    console.log('Session loaded.');
  }

  public async handleSession(context: BrowserContext) {
    AuthStarter.checkSessionDir();

    if (AuthStarter.isSessionExpired()) {
      console.log('Session expired or not found. Creating a new session...');
      await this.createSession();
    } else {
      console.log('Session is valid. Loading session...');
      await this.loadSession(context);
    }
  }
}
