Readme

Big Data Programming
Dozentin: Lisa Weinzierl
DHBW Ravensburg
RV-WWIDS120

Name Studierende: Luisa Ibele
Matrikelnummer: 8587535

Bitte senden Sie das Readme inkl. Screenshots für Lösungsskizze Aufgabe 1
Deadline: 26. August (via Poststempel oder Briefkasten Studiensekretariat) 


Aufgabe 1:
--> Siehe Screenshots (papierhaft / 8587535_PrüfungsleistungBDP.pdf)

Augabe 2:
Um eine real-time Graphik aus publizierten Sensorendaten einer Website zu erstellen, ist Stream/Real-Time Processing notwendig. Dazu wird als Big-Data-Architektur die event-zentrische Architektur einge-setzt. Bei dieser Architektur werden die Daten der Datenquelle (hier OpenWeatherMap) entgegenge-nommen und in einen Event Broker, welcher grundsätzlich eine hoch-skalierbare Publish/Subscribe Infrakstruktur darstellt, geschrieben. Dabei ermöglicht es die hohe Verfügbarkeit und Zuverlässigkeit des Event Brokers, dass die Daten von den Datenbanken in den Event Broker umgelagert werden und somit die Datenbanken nur ein Abbild der Daten aus dem Event Broker darstellen. Der Event Broker vermittelt dabei zwischen Producer, welcher Daten in Form von „Nachrichten“ publiziert, und Consu-mer, welcher diese Nachrichten empfängt, wodurch Producer und Consumer voneinander entkoppelt werden. Die Nachrichten zwischen Producer und Consumer werden dabei in sog. Topics, welche mehre-re Partitionen enthalten, gespeichert, wobei der Event Broker sicher stellt, dass keine der Nachrichten verloren geht und diese für die Consumer immer verfügbar sind.  
Generell ist Vorteil der event-zentrischen Architektur, dass eine höhere Agilität beim Präsentieren der Daten und eine konstante, stream-basierte Verarbeitung möglich ist. Auch ist diese Architektur zu-kunftsfähig, da sie bereit für natives Streaming ist, und dabei eine lose Kopplung von Datenquellen und Zielen ermöglicht. Nachteil ist, dass die Architektur sehr komplex ist, erst weniger Erfahrung damit vor-liegt und der Event Broker aufgrund seines „Single Source of Truth“ Seins und möglichen Ausfällen zur kritischen Komponente wird. Dadurch ist es wichtig, diesen zuverlässig aufzusetzen. Außerdem gibt der Event Broker aufgrund seiner Fähigkeiten auch das Design und den Aufbau der Architektur vor. 

Aufgabe 3:
Welche Variablen haben Sie verwendet?
- writer1, um Daten in das gewollte Kafka Topic (topic1) zu schreiben
- openWeatherMap, um auf die Funktionen der Klasse OpenWeatherMap zuzugreifen
- key, als fortlaufende Zahl für den Key für die abzuspeichernden Daten im Kafka Topic
- locs, um die Daten der load_locations Funktion zwischenzuspeichern
- response, um die Daten der get_forecast Funktion zwischenzuspeichern
- city, um jedem Dictionary die Stadt mit Name, Lattitude und Longitude hinzuzufügen

Welche Funktionen haben Sie verwendet?
- load_locations(), um die locations.json in ein json Objekt zu lesen
- collect_forecast_data(), um die Wetterdaten von der API zu holen und in Kafka abzuspeichern
- get_forecast() und im Rahmen dieser buil_url() von OpenWeatherMap.py, um die Wetterdaten von der API zu lesen
- retrieve() der Klasse KafkaReader in Kafka.py, um den Counter (key für die in Kafka abgespeicherten Daten) abhängig von der Länge der bereits gespeicherten Daten zu machen
- store() der Klasse KafkaWriter in Kafka.py, um Daten in Kafka zu speichern

Wie sind die Zusammenhänge?
Die Zusammenhänge für das Buffern der Daten in Kafka sehen wie folgt aus: Vor Aufruf der Funktion collect_forecast_data() werden KafkaWriter und KafkaReader für das zugehörige Topic (topic1) initialisiert und ein key, der die Länge / Größe der bereits in diesem Topic gespeicherten Daten darstellt, definiert. Innerhalb der Funktion wird als erstes die load_locations() Funktion aufgerufen und ihr Rückgabewert (das json Objekt der Städte für den Forecast) in einer Variable 'locs' gespeichert. Als nächstes wird über diese Liste an Locations geloopt. Dabei wird für jede Stadt in locs die get_forecast() Funktion der Klasse OpenWeatherMap aufgerufen und der Rückgabewert in 'response' gespeichert. Dabei wird get_forecast() die jeweilige Stadt übergeben, wodurch innerhalb der Funktion die zugehörige URL für die API von OpenWeatherMap zusammengesetzt wird und der Forecast für die nächsten fünf Tage von der API "geholt" wird. 'Response' stellt eine Liste an Dictionarys dar. Dabei wird über den Key 'list' von Response im nächsten Schritt geloopt. Innerhalb dieser for-Schleife werden die Stadt-Daten in der Variable 'city' als Dictionary abgespeichert und der Iterations-Variable 'res' hinzugefügt. Der Key für die in Kafka abzuspeichernden Daten wird um eins erhöht und 'res' wird zusammen mit diesem durch den writer1 in topic1 abgespeichert.
Später wird die collect_forecast_data() Funktion innerhalb einer Schleife intervallbasiert alle 15 Minuten aufgerufen. Dadurch werden die Forecast-Daten oft genug gelesen, um einen möglichen Service-Ausfall von beispielsweise einer Stunde zu kompensieren. Weil nicht ganz klar ist, wie oft OpenWeatherMap die Wetterdaten intervallbasiert aktualisiert (d.h. bspw. die Temperaturdaten mit der Zeit genauer werden), wurde ein Zeitraum von 15 Minuten gewählt, sodass zum einen die Aktualisierungen der Wetterdaten mit abgespeichert werden, zum anderen aber auch mögliche Ausfallrisiken kompensiert werden können. 

Welche Abhängigkeiten gibt es?
Allgemein ist die collect_forecast_data() Funktion von der load_locations() Funktion und der get_forecast() Funktion, beziehungsweise generell von der Klasse OpenWeatherMap, abhängig. Je nachdem, was diese Funktionen zurückliefern, kann diese die von den Funktionen zurückgelieferten Daten weiter verarbeiten.

Aufgabe 4:
Welche Variablen haben Sie verwendet? 
- writer2, um Daten in das cleane Topic zu speichern / schreiben
- reader1, um Daten aus dem ersten Topic (topic1) zu lesen
- all_data, um die Daten, die sich im ersten Topic (topic1) befinden, in einer Variable (Liste) zu speichern
- existing_data, um die Daten, die bereits im cleanen Topic (weather.forecast) existieren, in einer Liste zu speichern
- counter, als fortlaufende Zahl für den Key für die abzuspeichernden Daten in Kafka

Welche Funktionen haben Sie verwendet?
- cleaning(), um im ersten Topic (topic1) Dubletten auszumachen und die unique Werte in das zweite "cleane" Topic (weather.forecast) zu speichern.
- retrieve(), um auf die Daten in den zwei Topics zuzugreifen und diese in einer Liste zu speichern.

Wie sind die Zusammenhänge?
Die Zusammenhänge sehen für das Entfernen der Dubletten wie folgt als: als erstes wird außerhalb der Funktion ein zugehöriger KafkaWriter für das cleane Topic (weather.forecast) initialisiert, um später die Daten, aus welchen die Dubletten eliminiert wurden, dort abzuspeichern. Innerhalb der cleaning() Funktion werden erst die bestehenden Daten in topic1 in der Variable all_data und auch die existierenden Daten im Topic weather.forecast in der Variable existing_data abgespeichert, wobei beide Variablen eine Liste an Dictionarys darstellen. Auch wird ein Counter definiert, indem diesem die Länge von der existing_data Liste übergeben wird. In einem nächsten Schritt wird dann über all_data geloopt, wobei jedes Element in all_data ein Dictionary von Wetterdaten darstellt. Dabei wird für den Fall, dass in existing_data keine Daten vorhanden sind, erstmal mithilfe einer if-Abfrage überprüft, ob dies eine leere Liste darstellt. Wenn dies der Fall ist wird der Counter um eins erhöht, das erste Element a der Loop existing_data angehängt und im zugehörigen Topic (weather.forecast) mit dem Counter als Key abgespeichert. Hingegen wenn in existing_data bereits Daten existieren, so wird Else ausgeführt. Hier wird über die existing_data geloopt und dann mithilfe einer if-Abfrage gecheckt, ob das derzeitige a (von all_data) bereits in existing_data vorhanden ist. Ist dies nicht der Fall, so wird der Counter erhöht, a existing_data angehängt und im weather.forecast Topic abgespeichert. Zusammen mit collect_forecast_data() wird die cleaning() Funktion innerhalb einer while-Schleife alle 15 Minuten aufgerufen.
Idee hinter der Dubletten Erkennung ist es hier, die einzelnen Dictionary Elemente von all_data und existing_data so miteinander zu vergleichen, sodass Dubletten bei der Prüfung, ob ein Dictionary (a in all_data) bereits in existing_data ist, herausgefiltert werden. Da nicht ganz klar ist, wie oft die Wetterdaten auf OpenWeatherMap aktualisiert werden (im Sinne von: je näher der Tag, desto genauer die Wettervorhersage), werden die Dictionarys an Wettervorhersage komplett verglichen. Dadurch führen Änderungen / Aktualisierung der Wettervorhersage innerhalb der nächsten fünf Tage dazu, dass das "Wetter-Dictionary" des zugehörigen Forecast nicht als Dublette erkannt wird, da durch die Aktualisierung bspw. Temperatur, Windgeschwindigkeit oder Regen-Volumen nicht mehr überein stimmen und somit noch nicht in existing_data vorliegen. Dadurch ist gewährleistet, dass immer auch die aktuellste Vorhersage im weather.forecast Topic abgespeichert ist. Die gedoppelten Vorhersagen, die aufgrund der Aktualisierung der Wettervorhersage zustande kommen, werden später in der get_dataframe() Funktion vor weiterer Verarbeitung der Daten herausgefiltert.

Welche Abhängigkeiten gibt es?
Generell bestehen hier Abhängigkeiten in Bezug auf die Topics, in welchen die Wetterdaten gespeichert sind / werden sollen. Das bedeutet an dieser Stelle, dass die cleaning() Funktion in gewisser Weise von all_data und existing_data abhängig ist, da geprüft werden muss, welche (uniquen) Daten zum einen in all_data vorhanden sind und welche davon noch nicht in existing_data abgespeichert sind. Je nachdem, welche oder ob überhaupt Daten im ersten Topic (hier also: topic1) vorhanden sind, werden diese auf Dubletten gefiltert und diese in das cleane Topic (weather.forecast) gespeichert.

Aufgabe 5:
Welche Libraries verwenden Sie?
- datetime
- pandas
- plotly.express
- externe Libraries: Kafka (KafkaReader), statics

Wie kann Ihre Infographik vom Benutzer gelesen werden?
Allgemein informiert die vorliegende Infographik über die Wettervorhersage von verschiedenen Städten in Europa für die nächsten fünf Tage. Dabei kann der Benutzer in der Infographik die vorhergesagte Temperatur in °C für die verschiedenen Städte in Zeitintervallen von drei Stunden der nächsten fünf Tage ablesen. In der Infographik spiegelt auch die Farbe der Kreise der jeweiligen Stadt auch die Temperatur wider. Je roter der Kreis desto wärmer und je blauer desto kälter die vorhergesagte Temperatur (s. Color Scale rechts neben der Karte). Darüber hinaus wird neben der vorhergesagten Temperatur beim Hovern über die jeweilige Stadt auch ein Symbol der Wetterlage entsprechend und die gefühlte Temperatur angezeigt. Außerdem wird im "Hover-Text" die textuelle Beschreibung der jeweiligen Wetterlage angezeigt und eine Verhaltens- / Kleidungsempfehlung für den Benutzer ausgesprochen. Diese Empfehlung / dieser Tipp basiert auf der jeweiligen Wetterlage bezüglich auf die Temperatur, die Regen-/Gewitterlage, die Windgeschwindigkeit und die "Schneelage", wobei bei der Empfehlung auch beachtet wird, ob es sich um Tages- oder Nachtzeit bei der jeweiligen Vorhersage handelt. Über den Slider unterhalb der Infographik kann der Benutzer dann die gesamte Wettervorhersage für die nächsten fünf Tage in den Zeitintervallen von drei Stunden abspielen lassen.

Aufgabe 6:
Welche Libraries verwenden Sie?
- datetime
- time
- pandas
- plotly.express
- IPython
- externe Libraries: Kafka (KafkaReader), statics

Welche Änderungen waren im Vergleich zur Aufgabe 5 notwendig?
Im Gegensatz zu Aufgabe 5 wird die Funktion, um aus den in Kafka abgespeicherten Daten eine Infographik darzustellen, im Rahmen einer while Schleife aufgerufen. Dadurch geschieht der Funktionsaufruf für die Infographik mithilfe eines Timers (time.sleep()) alle 15 Sekunden. Vor dem Aufruf der Infographik-Funktion wird der Output mithilfe von IPython.display (clear_output) "geleert", damit die Infographik aktualisiert werden kann und nicht immer eine neue Graphik geplottet wird. Dadurch ist insgesamt gewährleistet, dass sie die Werte bei Erneuerung der Messung, wie zum Beispiel Erneuerung der Temperatur in einer Stadt, automatisch aktualisieren und somit immer die aktuellen Daten der Wettervorhersage in der Infographik dem Benutzer zur Verfügung stehen.