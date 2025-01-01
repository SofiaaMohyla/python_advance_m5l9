from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Artifact, Stalker
from rest_framework.test import APITestCase

class ArtifactModelTest(TestCase):
    def setUp(self):
        # Створення тестового об'єкта Artifact
        self.artifact = Artifact.objects.create(
            name="Crystal Shard",
            description="A rare and mysterious shard.",
            rarity="Legendary",
            radiation_level=12.5,
            value=10000
        )

    def test_artifact_creation(self):
        """
        Перевірка, чи створюється об'єкт Artifact правильно
        """
        artifact = self.artifact
        self.assertEqual(artifact.name, "Crystal Shard")
        self.assertEqual(artifact.description, "A rare and mysterious shard.")
        self.assertEqual(artifact.rarity, "Legendary")
        self.assertAlmostEqual(artifact.radiation_level, 12.5)
        self.assertEqual(artifact.value, 10000)

    def test_str_method(self):
        """
        Перевірка методу __str__()
        """
        artifact = self.artifact
        self.assertEqual(str(artifact), "Crystal Shard")

    def test_radiation_level_positive(self):
        """
        Перевірка, що рівень радіації додатний
        """
        artifact = self.artifact
        self.assertGreater(artifact.radiation_level, 0)

    def test_value_positive_integer(self):
        """
        Перевірка, що значення artifact є додатним цілим числом
        """
        artifact = self.artifact
        self.assertGreater(artifact.value, 0)

    def test_name_max_length(self):
        """
        Перевірка, чи обмеження довжини імені працює
        """
        artifact = Artifact(
            name="a" * 101,  # 101 символ
            description="Test description",
            rarity="Common",
            radiation_level=1.0,
            value=10
        )
        with self.assertRaises(ValidationError):
            artifact.full_clean()
            artifact.save()


