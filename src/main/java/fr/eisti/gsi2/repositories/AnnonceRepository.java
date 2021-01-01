package fr.eisti.gsi2.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import fr.eisti.gsi2.entities.AnnonceEntity;

public interface AnnonceRepository extends JpaRepository<AnnonceEntity,Long> {
	
}
