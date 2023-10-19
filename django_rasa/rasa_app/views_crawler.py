from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from elasticsearch import Elasticsearch
import os
from django.contrib.auth.decorators import login_required
from django.conf import settings
ELASTICSEARCH_HOST = 'localhost'  # Aggiunto qui
ELASTICSEARCH_PORT = 9200  # Ag


@login_required
def search_view(request):
    query = request.GET.get('q', '')
    es = Elasticsearch([f"http://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}"])
    results = es.search(index="documenti_server", body={
        "query": {
            "match": {
                "path": query  # Puoi cambiare "path" con il campo appropriato se necessario
            }
        }
    })

    # Estrai i percorsi dei file dai risultati di Elasticsearch
    file_paths = [hit['_source']['path'] for hit in results['hits']['hits']]

    context = {
        'file_paths': file_paths
    }

    return render(request, 'search_results.html', context)


def download_file(request, file_path):
    print(f"file_path ricevuto: {file_path}")
    if not file_path.startswith('/'):
        file_path = '/' + file_path

    absolute_file_path = os.path.join(settings.BASE_DIR, file_path)  # Usiamo settings.BASE_DIR

    # Assicurati di gestire le questioni di sicurezza
    with open(absolute_file_path, 'rb') as file:  # Usiamo absolute_file_path qui
        response = HttpResponse(
            file.read(), content_type="application/octet-stream")
        response['Content-Disposition'] = 'inline; filename=' + \
            os.path.basename(file_path)
        return response

