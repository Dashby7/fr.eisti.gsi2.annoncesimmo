package fr.eisti.gsi2.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import fr.eisti.gsi2.dto.Annonce;
import fr.eisti.gsi2.entities.AnnonceEntity;
import fr.eisti.gsi2.mapper.AnnonceMapper;
import fr.eisti.gsi2.services.AnnonceService;

@Controller
public class AnnonceController {

	@Autowired
	private AnnonceService annonceService;

	@Autowired
	private AnnonceMapper annonceMapper;

	// Lancer la page d'accueil HTML (dans le répertoire templates)
	@GetMapping("/index")
	public String index(Model model) {
		List<Annonce> list = this.getAllAnnonces();
		model.addAttribute("annoncesListes", list);
		return "index";
	}

	// Rediriger vers la page d'accueil
	@GetMapping
	public String indexRedir() {
		return "redirect:/index";
	}

	// Récupérer une annonce via son ID
	@GetMapping("/annonces/{id}")
	@ResponseBody
	public Annonce getAnnonceById(@PathVariable Long id) {
		return annonceMapper.mapToDTO(annonceService.getAnnonceById(id).orElseThrow());
	}

	// Récupérer toutes les annonces existantes
	@GetMapping("/annonces")
	@ResponseBody
	public List<Annonce> getAllAnnonces() {
		return annonceMapper.mapToDTO(annonceService.getAllAnnonces());
	}

	// Récupérer le nombre d'annonces existantes
	@GetMapping("/annonces/count")
	@ResponseBody
	public Long countAllAnnonces() {
		return annonceService.countAllAnnonces();
	}

	// Retourne vrai ou faux selon si une annonce existe ou non
	@GetMapping("/annonces/exists/{id}")
	@ResponseBody
	public boolean existAnnonceById(@PathVariable Long id) {
		return annonceService.existAnnonceById(id);
	}

	// Enregistrer une nouvelle annonce
	@PostMapping("/annonces")
	@ResponseBody
	public AnnonceEntity saveAnnonce(@RequestBody Annonce annonce) {
		return annonceService.saveOrUpdate(annonceMapper.mapToEntity(annonce));
	}

	// Mettre à jour une annonce
	@PutMapping("/annonces")
	@ResponseBody
	public AnnonceEntity updateAnnonce(@RequestBody Annonce annonce) {
		return annonceService.saveOrUpdate(annonceMapper.mapToEntity(annonce));
	}

	// Supprimer une annonce
	@DeleteMapping("/annonces/{id}")
	@ResponseBody
	public void deleteAnnonce(@PathVariable Long id) {
		annonceService.deleteAnnonceById(id);
	}

	// Rechercher des annonces par critères
	@GetMapping("/annoncesRecherches")
	@ResponseBody
	public List<AnnonceEntity> findParCriteres(@RequestParam(value = "codePostal", required = false) String codePostal,
			@RequestParam(value = "typeBien", required = false) String typeBien,
			@RequestParam(value = "typeTransaction", required = false) String typeTransaction,
			@RequestParam(value = "prixMin", required = false) Integer prixMin,
			@RequestParam(value = "prixMax", required = false) Integer prixMax,
			@RequestParam(value = "surfaceMin", required = false) Integer surfaceMin,
			@RequestParam(value = "surfaceMax", required = false) Integer surfaceMax) {

		if (prixMin == null)
			prixMin = 0;
		if (surfaceMin == null)
			surfaceMin = 0;

		return annonceService.findByCriteres(codePostal, typeBien, typeTransaction, prixMin, prixMax, surfaceMin,
				surfaceMax);
	}

	// Rechercher toutes les annonces par prix croissant
	@GetMapping("/annoncesParPrixAsc")
	@ResponseBody
	public List<AnnonceEntity> getAnnoncesOrderByPrixAsc() {
		return annonceService.getAnnoncesOrderByPrixAsc();
	}

	// Rechercher toutes les annonces par prix décroissant
	@GetMapping("/annoncesParPrixDesc")
	@ResponseBody
	public List<AnnonceEntity> getAnnoncesOrderByPrixDesc() {
		return annonceService.getAnnoncesOrderByPrixDesc();
	}

	// Rechercher toutes les annonces par surface croissante
	@GetMapping("/annoncesParSurfaceAsc")
	@ResponseBody
	public List<AnnonceEntity> getAnnoncesOrderBySurfaceAsc() {
		return annonceService.getAnnoncesOrderBySurfaceAsc();
	}

	// Rechercher toutes les annonces par surface décroissante
	@GetMapping("/annoncesParSurfaceDesc")
	@ResponseBody
	public List<AnnonceEntity> getAnnoncesOrderBySurfaceDesc() {
		return annonceService.getAnnoncesOrderBySurfaceDesc();
	}

}
