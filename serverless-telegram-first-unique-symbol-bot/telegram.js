const axios = require('axios');

const TOKEN = process.env.TELEGRAM_TOKEN;


module.exports.sendMessage = params => {
    const baseUrl = `https://api.telegram.org/bot${TOKEN}/sendMessage`;

    return axios
        .get(baseUrl, { params})   //, proxy })
        .catch(e => {
            console.error('Telegram error', e.response.data);
        });
};
