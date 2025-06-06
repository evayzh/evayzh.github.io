import express from 'express';

const app = express();
const port = 3001;

// Serve static files with default directory listing, just like Python's SimpleHTTPRequestHandler
app.use(express.static('docs', {
    extensions: ['html', 'htm'], // Try these extensions for extensionless URLs
    index: 'index.html'         // Default file for directory requests
}));

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
