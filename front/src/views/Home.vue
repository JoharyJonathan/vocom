<template>
    <main>
        <h1>Home</h1>

          <div>
            <button @click="startListening">🎤 Rechercher par voix</button>
            <p>Texte reconnu : {{ transcript }}</p>
        </div>
    </main>
</template>

<script>
    export default {
        name: "Home",
        data() {
            return {
            transcript: ''
            }
        },
        methods: {
            startListening() {
            const recognition = new window.webkitSpeechRecognition() || new window.SpeechRecognition();
            recognition.lang = 'fr-FR';
            recognition.interimResults = false;
            recognition.maxAlternatives = 1;

            recognition.start();

            recognition.onresult = (event) => {
                this.transcript = event.results[0][0].transcript;
                this.searchProducts(this.transcript);
            };

            recognition.onerror = (event) => {
                console.error("Erreur reconnaissance vocale:", event.error);
            };
            },
            searchProducts(query) {
            fetch(`/search?query=${encodeURIComponent(query)}`)
                .then(res => res.json())
                .then(data => {
                console.log("Résultats:", data);
                });
            }
        }
    }
</script>