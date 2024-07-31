document.getElementById('translation-form').addEventListener('submit', function(event) {
    event.preventDefault();

    let sourceText = document.getElementById('source_text').value;
    let sourceLanguage = document.getElementById('source_language').value;
    let targetLanguage = document.getElementById('target_language').value;

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `source_text=${sourceText}&source_language=${sourceLanguage}&target_language=${targetLanguage}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('translated_text').innerText = data.translated_text;
    });
});
