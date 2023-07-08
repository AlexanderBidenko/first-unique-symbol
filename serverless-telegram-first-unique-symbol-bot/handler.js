const telegram = require('./telegram');

function countOccurrences(array, targetElement) {
    let count = 0;
    for (let i = 0; i < array.length; i++) {
        if (array[i] === targetElement) {
        count++;
        }
    }
    return count;
}

function first_unic_symbol(input_text) {
    const regex = /\b\w+\b/g;
    const words = input_text.match(regex);
    console.log(words)
    let symbols = []

    for (let i = 0; i < words.length; i++) {
        for (let j = 0; j < words[i].length; j++) {
                if (countOccurrences(words[i], words[i][j]) === 1) {
                    symbols.push(words[i][j])

                    break
            }
        }
    }
    console.log(symbols)
    for (let i = 0; i < symbols.length; i++) {
        if (countOccurrences(symbols, symbols[i]) === 1) {
            console.log(symbols[i])
            return symbols[i]
        }
    }

    return 'No unique symbols'
}

module.exports.processWebhook = async event => {
    const body = JSON.parse(event.body);
    if (body && body.message) {
        try {
            let { chat, text } = body.message;
            if ((typeof(text) !== 'undefined') && (typeof(text) !== undefined)) {
                
                let answer = first_unic_symbol(text)
                
                if (answer.length === 1) {
                    await telegram.sendMessage({ chat_id: chat.id, text: `First unique symbol from unique symbols: ${answer}` });
                } else {
                    await telegram.sendMessage({ chat_id: chat.id, text: answer });
                }                
            }
        } catch (e) { 
            await telegram.sendMessage({ chat_id: chat.id, text: `${toString(e)}` });
        }
        return { statusCode: 200 };
    };
}
