package fr.eisti.gsi2.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import fr.eisti.gsi2.entities.AnnonceEntity;

public interface AnnonceRepository extends JpaRepository<AnnonceEntity,Long> {
	
	/*@Query(value = "SELECT * FROM immobilier.annonce WHERE code_postal = :codePostal AND type_bien = :typeBien AND type_transaction = :typeTransaction "
			+ "AND prix BETWEEN :prixMin AND :prixMax AND surface BETWEEN :surfaceMin AND :surfaceMax", nativeQuery = true)
	List<AnnonceEntity> findByCriteres(
			@Param("codePostal") String codePostal, 
			@Param("typeBien") String typeBien, 
			@Param("typeTransaction") String typeTransaction,
			@Param("prixMin") int prixMin, 
			@Param("prixMax") int prixMax, 
			@Param("surfaceMin") int surfaceMin, 
			@Param("surfaceMax") int surfaceMax);*/
	
}
