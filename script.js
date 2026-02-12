// Importar bibliotecas
const express = require("express");
const fetch = require("node-fetch"); // Para fazer requisições HTTP
const cors = require("cors");         // Para permitir chamadas do frontend
require("dotenv").config();           // Para ler a chave do arquivo .env

// Criar app Express
const app = express();

// Middlewares
app.use(cors());              // Permite que qualquer frontend acesse
app.use(express.json());      // Permite ler JSON no corpo da requisição

// Rota principal da IA
app.post("/api/solve", async (req, res) => {
    const { prompt } = req.body; // Recebe o texto do usuário

    try {
        // Chamada para OpenAI API
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${process.env.OPENAI_API_KEY}` // chave segura no Railway
            },
            body: JSON.stringify({
                model: "gpt-4",
                messages: [
                    { role: "system", content: "Você é um professor de matemática avançada. Explique passo a passo." },
                    { role: "user", content: prompt }
                ],
                max_tokens: 500
            })
        });

        const data = await response.json();

        // Envia a resposta da OpenAI para o frontend
        res.json({ answer: data.choices[0].message.content });

    } catch (err) {
        console.error(err);
        res.status(500).json({ error: "Erro ao consultar OpenAI" });
    }
});

// Porta do servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
