import React, { useState } from 'react';

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState([]);

  const handleInputChange = (event) => {
    setQuestion(event.target.value);
  };

   const handleSubmit = async (event) => {
  event.preventDefault();

  const res = await fetch('http://127.0.0.1:5000/professions');
  const data = await res.json();
  
  console.log(data);  // API cavabını konsola yazdıraq
  setResponse(data);  // Cavabı state-ə təyin edirik
};


  return (
    <div>
      <h1>İxtisas Seçimi</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={handleInputChange}
          placeholder="Suallarınızı yazın"
        />
        <button type="submit">Sorğu Göndər</button>
      </form>

      <div>
        <h2>Cavablar</h2>
        {response.length > 0 ? (
          response.map((item, index) => (
            <div key={index}>
              <h3>{item["İxtisas Adı"]}</h3>
              <p>{item["Təhsil Müddəti"]}</p>
              <p>{item["Müəssisə"]}</p>
            </div>
          ))
        ) : (
          <p>Cavab yoxdur</p>
        )}
      </div>
    </div>
  );
}

export default App;
