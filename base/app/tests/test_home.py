from http import HTTPStatus

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from pytest_django.asserts import assertTemplateUsed, assertContains

from base.app.models import Produto

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

@pytest.fixture
def resp(client):
    Produto.objects.create(produto='blusa', preco=100000, descricao='vestido azul', foto=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'))
    return client.get('/')

def test_status_code(resp):
    assert resp.status_code == HTTPStatus.OK
    assertTemplateUsed(resp, 'home.html')

def test_template_content(resp):
    assertContains(resp, 'vestido azul', 1)
    assertContains(resp, 'blusa', 1)
    assertContains(resp, '100000', 1)
    assertContains(resp, '<img src="/media/test_image_', 1)





