import { chromium, firefox, webkit, BrowserType, BrowserContext, Browser } from '@playwright/test';

interface GlobalContext {
    __BROWSER_CONTEXT__?: BrowserContext;
    __BROWSER__?: Browser;
}

declare const global: GlobalContext;

const browserTypes: Record<string, BrowserType> = {
    chromium,
    firefox,
    webkit,
};

export default async function globalSetup(): Promise<void> {
    const browserName = process.env.BROWSER || 'chromium'; // Default to Chromium
    const env = process.env.ENV || 'local'; // Default to local environment
    const setup = process.env.SETUP || ''; // Default to headless mode

    const browserType = browserTypes[browserName.toLowerCase()];
    if (!browserType) {
        throw new Error(`Unsupported browser: ${browserName}`);
    }

    const isLocal = env === 'local';
    const isHeaded = setup === '--headed';

    // Launch the browser
    const browser = await browserType.launch({
        headless: !isHeaded,
        args: isLocal && isHeaded ? ['--start-maximized'] : [],
    });

    // Save the context state globally for reuse
    global.__BROWSER_CONTEXT__ = await browser.newContext(
        isHeaded ? {} : { viewport: { width: 1920, height: 1080 } }
    );
    global.__BROWSER__ = browser;
}
