package fr.eisti.gsi2.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import fr.eisti.gsi2.entities.AnnonceEntity;
import fr.eisti.gsi2.repositories.AnnonceRepository;

@Service
public class AnnonceService {

	  @Autowired
	  private AnnonceRepository annonceRepository;

	  @Transactional
	  public Optional<AnnonceEntity> getAnnonceById(Long id) {
	    return annonceRepository.findById(id);
	  }
	  
	  @Transactional
	  public List<AnnonceEntity> getAllAnnonces() {
	    return annonceRepository.findAll();
	  }
	  
	  @Transactional
	  public long countAllAnnonces() {
	    return annonceRepository.count();
	  }
	  
	  @Transactional
	  public boolean existAnnonceById(Long id) {
	    return annonceRepository.existsById(id);
	  }
	  
	  @Transactional
	  public AnnonceEntity saveOrUpdate(AnnonceEntity annonce) {
	    return annonceRepository.save(annonce);
	  }
	  
	  @Transactional
	  public void deleteAnnonce(AnnonceEntity annonce) {
	    annonceRepository.delete(annonce);
	  }
	  
	  @Transactional
	  public void deleteAnnonceById(Long id) {
	    annonceRepository.deleteById(id);
	  }
	  /*
	  EN COURS
	  @Transactional
	  public List<AnnonceEntity> findByCriteres(String codePostal, String typeBien, String typeTransaction, int prixMin, int prixMax, int surfaceMin, int surfaceMax) {
		  return annonceRepository.findByCriteres(codePostal, typeBien, typeTransaction, prixMin, prixMax, surfaceMin, surfaceMax);
	  }*/
}