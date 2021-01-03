package fr.eisti.gsi2.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import fr.eisti.gsi2.entities.AnnonceEntity;

public interface AnnonceRepository extends JpaRepository<AnnonceEntity,Long> {
	
	// Spécification de la méthode de requête par critères
	@Query(value = "SELECT * FROM immobilier.annonce "
			+ "WHERE (:codePostal is null or code_postal = :codePostal) "
			+ "AND (:typeBien is null or type_bien = :typeBien) "
			+ "AND (:typeTransaction is null or type_transaction = :typeTransaction) "
			+ "AND (:prixMax is null or (prix BETWEEN :prixMin AND :prixMax)) "
			+ "AND (:surfaceMax is null or (surface BETWEEN :surfaceMin AND :surfaceMax))", 
			nativeQuery = true)
	List<AnnonceEntity> findByCriteres(
			@Param("codePostal") String codePostal, 
			@Param("typeBien") String typeBien, 
			@Param("typeTransaction") String typeTransaction,
			@Param("prixMin") Integer prixMin, 
			@Param("prixMax") Integer prixMax, 
			@Param("surfaceMin") Integer surfaceMin, 
			@Param("surfaceMax") Integer surfaceMax);
}
