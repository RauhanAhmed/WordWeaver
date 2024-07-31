document.getElementById('analyzerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let sourceText = document.getElementById('source_text').value;

    fetch('/analyzer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `source_text=${sourceText}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('polarity').innerText = "Polarity: " + data.polarity;
        document.getElementById('polarityScore').innerText = "Polarity Score: " + data.polarityScore;
        document.getElementById('subjectivityScore').innerText = "Subjectivity Score: " + data.subjectivityScore;
    });
});
