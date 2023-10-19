PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    info TEXT
);
INSERT INTO people VALUES(2,'Mario Rossi','E'' solo un nome d''esempio presente nel database.');
INSERT INTO people VALUES(3,'Titina Iannucci','È mia moglie, e guai a chi me la tocca!');
INSERT INTO people VALUES(4,'Angela Rocchia','E'' un''insegnante della scuola primaria, responsabile della funzione strumentale sull''aggiornamento del PTOF, incaricata delle prove invalsi e del sistema di valutazione della scuola');
INSERT INTO people VALUES(5,'Mariantonietta del MOnte','E'' la vicepreside vicaria della scuola, con delega al cordinamento della scuola primaria.');
INSERT INTO people VALUES(6,'Cristina Becci','Appartiene allo Staff di Presidenza, vicepreside con delega del coordinamento della scuola secondaria di 1° grado');
INSERT INTO people VALUES(7,'Lucia Palmieri','Cordinatrice del plesso della primaria di Nuova Cliternia');
INSERT INTO people VALUES(8,'Olga Fraccacreta','Coordinatrice della scuola dell''infanzia');
INSERT INTO people VALUES(9,'Pierluca De Filippis','Fa parte dello staff di presidenza, è vicpreside con icnarido di coordinatore della scuola secondaria di grado.');
INSERT INTO people VALUES(10,'Teresa Messina','E'' la Segretaria della scuola. O meglio la DSGA, direttrice dei servizi generali e ammnistrativi.');
INSERT INTO people VALUES(11,'Christian Ronzullo','Insegnante di sostegno per la scuola secondaria di 1° grado. E'' stato coordinatore degli insegnanti di sostegno, oggi cura progetti legati all''orienteering. ');
INSERT INTO people VALUES(12,'Maria Giovanna Carriera','Insegnante di sostegno per la scuola primaria, oggi fa parte dello staff di presidenza come responsabile coordinatrice degli insegnanti di sostegno per la primaria. ');
INSERT INTO people VALUES(13,'Luciana Fortunato','Insegnante di sostegno per la scuola primaria, oggi responsabile della funzione strumentale n.3 come coordinatrice degli alunni con disturbi specifici di apprendimento (DSA), con bisogni educativi speciali (BES) e con altre fragilità');
INSERT INTO people VALUES(14,'remo ianniruberto','Docente di strumento musicale, violoncello, responsabile coordinatore dei professori di strumento.');
INSERT INTO people VALUES(15,'rosanna fanzo','Docente di pianoforte per i ragazzi della scuola media di 1° grado');
INSERT INTO people VALUES(16,'paolo castellitto','Docente di Violino della scuola secondaria di 1° grado.');
INSERT INTO people VALUES(17,'stefania bovino','Insegnante primaria, animatrice digitale e titolare della funzione strumentale n.2 di sostegno alle nuove tecnologie.');
INSERT INTO people VALUES(18,'titina iannucci','E'' mia moglie e guai a chi me la tocca.');
INSERT INTO people VALUES(19,'cristina becci','E'' la vicepreside, coordinatricr la scuola secondaria di 1° grado. ');
INSERT INTO people VALUES(20,'luciana fortunato','Insegnante di Sostegno, responsabile per i DSA, ragazzi con disturbi specifici di apprendimento, BES, ragazzi con bisogni speciali e tutti gli altri ragazzi con fragilità.');
INSERT INTO people VALUES(21,'Mario Rossi','E'' solo un nome d''esempio presente nel database.');
INSERT INTO people VALUES(22,'Titina Iannucci','È mia moglie, e guai a chi me la tocca!');
INSERT INTO people VALUES(23,'Angela Rocchia','E'' un''insegnante della scuola primaria, responsabile della funzione strumentale sull''aggiornamento del PTOF, incaricata delle prove invalsi e del sistema di valutazione della scuola');
INSERT INTO people VALUES(24,'Mariantonietta del Monte','E'' la vicepreside vicaria della scuola, con delega al cordinamento della scuola primaria.');
INSERT INTO people VALUES(25,'Cristina Becci','Appartiene allo Staff di Presidenza, vicepreside con delega del coordinamento della scuola secondaria di 1° grado');
INSERT INTO people VALUES(26,'Lucia Palmieri','Cordinatrice del plesso della primaria di Nuova Cliternia');
INSERT INTO people VALUES(27,'Olga Fraccacreta','Coordinatrice della scuola dell''infanzia');
INSERT INTO people VALUES(28,'rosa loffreda','è la vice segretaria della scuola');
INSERT INTO people VALUES(29,'patrizia fiore','è un''assistente amministrativa, ex insegnante di scuola primaria, andata fra gli amministrativi per inidoneità');
INSERT INTO people VALUES(30,'annamaria saracino','E'' una assistenta amministrativa, si occupa del settore della didattica');
INSERT INTO people VALUES(34,'mariantonieta del monte','E'' la vicepreside dalla primaria, ha la delega come vicaria della scuola. E'' segretaria del collegio dei docenti e si occupa delle attività dei progetti pon.');
INSERT INTO people VALUES(35,'giuseppe iannucci','E'' il fratello di mia moglie titina iannucci');
INSERT INTO people VALUES(36,'luigi coppola','E'' il nipote di mia moglie ed è il figlio di Anna Iannucci e Donato Coppola');
INSERT INTO people VALUES(37,'teresa riccardi','E'' la mamma di Titina iannucci');
COMMIT;
