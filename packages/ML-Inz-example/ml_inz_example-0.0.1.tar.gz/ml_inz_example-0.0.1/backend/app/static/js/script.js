document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('queryForm');
    const loadingIndicator = document.getElementById('loading');
    const responseContainer = document.getElementById('response');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Показать анимацию загрузки
        loadingIndicator.style.display = 'inline-block';
        responseContainer.style.display = 'none';

        const question = document.getElementById('question').value;
        const documentText = document.getElementById('document').value;

        fetch('/query/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: question,
                document: documentText
            })
        })
        .then(response => response.json())
        .then(data => {
            // Скрыть анимацию загрузки
            loadingIndicator.style.display = 'none';

            // Показать ответ
            responseContainer.style.display = 'block';
            responseContainer.innerText = data.response;
        })
        .catch(error => {
            console.error('Error:', error);
            loadingIndicator.style.display = 'none';
            responseContainer.style.display = 'block';
            responseContainer.innerText = 'An error occurred. Please try again.';
        });
    });
});
