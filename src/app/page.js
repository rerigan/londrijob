// app/page.js
'use client'

import { useEffect, useState } from 'react';

export default function Home() {
  const [vagas, setVagas] = useState([]);

  useEffect(() => {
    fetch('/vagas.json')
      .then((res) => res.json())
      .then((data) => setVagas(data));
  }, []);

  return (
    <main className="p-6 max-w-2xl mx-auto">
      <h1 className="title text-6xl font-bold mb-4 text-center mt-20 mb-20"><a href='#'>LondriJob</a></h1>
      <h3 className="text-xl font-bold mb-10 text-center">Vagas de emprego em Londrina</h3>
      <h4 className="text-md mb-10 text-center">As vagas a seguir são as vagas mais recentes recolhidas de diversos sites, diariamente.</h4>
      {vagas.length === 0 ? (
        <p className='text-center'>Carregando vagas...</p>
      ) : (
        <ul className="botaovaga space-y-5">
          {vagas.map((vaga, index) => (
            <a
            href={vaga.link}
            target="_blank"
            rel="noopener noreferrer"
            className="text-white p-6 font-bold" key={index}
          >
            <li key={index} className="botaoovaga border p-8 rounded transition text-center">
              
                {vaga.titulo}
             
            </li>
            </a>
          ))}
        </ul>
      )}
      <div><h3 className='text-center font-bold mt-20 mb-10'><a href='https://www.instagram.com/reri.gan'>Desenvolvido por Rerigan</a></h3></div>
    </main>
  );
}