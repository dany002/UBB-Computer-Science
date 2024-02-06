const appendLog = (message) => {
    try {
        const timestamp = new Date().toISOString();
        const logMessage = `${timestamp}: ${message}`;

        console.log(logMessage);
    } catch (e) {
        console.error('Failed to log message', e);
    }
};

export {appendLog};