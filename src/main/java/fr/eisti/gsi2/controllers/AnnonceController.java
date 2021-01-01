package fr.eisti.gsi2.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import fr.eisti.gsi2.dto.Annonce;
import fr.eisti.gsi2.entities.AnnonceEntity;
import fr.eisti.gsi2.mapper.AnnonceMapper;
import fr.eisti.gsi2.services.AnnonceService;

@RestController
public class AnnonceController {
	
	@Autowired
	private AnnonceService annonceService;
	
	@Autowired
	private AnnonceMapper annonceMapper;

	@GetMapping("/annonces/{id}")
	public Annonce getAnnonceById(@PathVariable Long id) {
		return annonceMapper.mapToDTO(annonceService.getAnnonceById(id).orElseThrow());
	}
	
	@GetMapping("/annonces")
	public List<Annonce> getAllAnnonces() {
		return annonceMapper.mapToDTO(annonceService.getAllAnnonces());
	}
	
	@GetMapping("/annonces/count")
	public Long countAllAnnonces() {
		return annonceService.countAllAnnonces();
	}
	
	@GetMapping("/annonces/exists/{id}")
	public boolean existAnnonceById(@PathVariable Long id) {
		return annonceService.existAnnonceById(id);
	}
	
	@PostMapping("/annonces")
	public AnnonceEntity saveAnnonce(@RequestBody Annonce annonce) {
		return annonceService.saveOrUpdate(annonceMapper.mapToEntity(annonce));
	}
	
	@PutMapping("/annonces")
	public AnnonceEntity updateAnnonce(@RequestBody Annonce annonce) {
		return annonceService.saveOrUpdate(annonceMapper.mapToEntity(annonce));
	}
	
	@DeleteMapping("/annonces/{id}")
	public void deleteAnnonce(@PathVariable Long id) {
		annonceService.deleteAnnonceById(id);
	}
}
