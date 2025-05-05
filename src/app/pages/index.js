// pages/index.js
import { useEffect, useState } from 'react';

export default function Home() {
  const [vagas, setVagas] = useState([]);

  useEffect(() => {
    fetch('/vagas.json')
      .then((res) => res.json())
      .then((data) => setVagas(data));
  }, []);

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Vagas Disponíveis</h1>
      {vagas.length === 0 ? (
        <p>Carregando vagas...</p>
      ) : (
        <ul className="space-y-3">
          {vagas.map((vaga, index) => (
            <li key={index} className="border p-3 rounded hover:bg-gray-100 transition">
              <a
                href={vaga.link}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:underline"
              >
                {vaga.titulo}
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}