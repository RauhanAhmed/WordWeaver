document.getElementById('summarizerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let sourceText = document.getElementById('source_text').value;

    fetch('/summarizer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `source_text=${sourceText}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('summary').innerText = data.summary;
    });
});
