import { chromium, firefox, webkit } from '@playwright/test';

module.exports = async (config) => {
    const browserName = process.env.BROWSER || 'chromium'; // Default to Chromium
    const env = process.env.ENV || 'local'; // Default to local environment
    const setup = process.env.SETUP || ''; // Default to headless mode

    let browserType;
    switch (browserName.toLowerCase()) {
        case 'chromium':
        case 'chrome':
            browserType = chromium;
            break;
        case 'firefox':
            browserType = firefox;
            break;
        case 'webkit':
            browserType = webkit;
            break;
        default:
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
        isHeaded ? {} : {viewport: {width: 1920, height: 1080}}
    );
    global.__BROWSER__ = browser;
};