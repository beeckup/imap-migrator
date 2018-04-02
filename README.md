migrate-imap-account-to-gmail
=============================

Progetto scritto in python per la migrazione mail via imap

Posizionarsi nella cartella deploy_migrator, copiare il file docker-compose.sample.yml in docker-compose.yml e modificare le variabili d'ambiente per la migrazione della casella (si può creare un container per ogni casella email. Se il container crasha basta riavviare e la migrazione riprende dal punto in cui era)

Uso
---

Una volta sistemato il file compose, lanciarlo con

```bash
docker-compose up
```

A fine migrazione, si avrà un messaggio come questo:

    Synchronization of 12571 messages finished, took 6:44:35.101650
