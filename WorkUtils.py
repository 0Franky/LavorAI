def workDecoder(numberWork):
  if numberWork == 1:
    return ["Insegnate", "Comunicativo"]

  if numberWork == 2:
    return ["Avvocato", "Comunicativo"]

  if numberWork == 3:
    return ["Marketing", "Comunicativo"]


  if numberWork == 4:
    return ["Informatico/Ingegnere", "Tecnico"]

  if numberWork == 5:
    return ["Bancario", "Tecnico"]

  if numberWork == 6:
    return ["Amministrazione", "Tecnico"]


  if numberWork == 7:
    return ["Scienziato di laboratorio/Operatore sanitario", "Pratico"]

  if numberWork == 8:
    return ["Operaio/Artigiano", "Pratico"]

  if numberWork == 9:
    return ["Forze dell'ordine/Sicurezza", "Pratico"]


  if numberWork == 10:
    return ["Personal Trainer", "Sportivo"]

  if numberWork == 11:
    return ["Ballerino", "Sportivo"]

  if numberWork == 12:
    return ["Atleta", "Sportivo"]


  if numberWork == 12:
    return ["Musicista", "Creativo"]

  if numberWork == 14:
    return ["Designer", "Creativo"]

  if numberWork == 15:
    return ["Scrittore", "Creativo"]
  
  return ["Errore!", "Errore!"]