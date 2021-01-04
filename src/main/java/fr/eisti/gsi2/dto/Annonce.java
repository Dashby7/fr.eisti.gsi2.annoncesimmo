package fr.eisti.gsi2.dto;

import java.io.Serializable;

public class Annonce implements Serializable {

	private static final long serialVersionUID = -2714400156157011932L;

	private Long id;

	private String nomAnnonce;

	private String ville;

	private String adresse;

	private String codePostal;

	private int prix;

	private String prixString;

	private int surface;

	private String divisibilite;

	private String disponibilite;

	private String typeTransaction;

	private String typeBien;

	private String lien;

	private String lienPhoto;

	private String contact;

	private String site;

	private String referenceSite;

	private String indicationPrix;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getNomAnnonce() {
		return nomAnnonce;
	}

	public void setNomAnnonce(String nomAnnonce) {
		this.nomAnnonce = nomAnnonce;
	}

	public String getVille() {
		return ville;
	}

	public void setVille(String ville) {
		this.ville = ville;
	}

	public String getAdresse() {
		return adresse;
	}

	public void setAdresse(String adresse) {
		this.adresse = adresse;
	}

	public String getCodePostal() {
		return codePostal;
	}

	public void setCodePostal(String codePostal) {
		this.codePostal = codePostal;
	}

	public int getPrix() {
		return prix;
	}

	public void setPrix(int prix) {
		this.prix = prix;
	}

	public String getPrixString() {
		return prixString;
	}

	public void setPrixString(String prixString) {
		this.prixString = prixString;
	}

	public int getSurface() {
		return surface;
	}

	public void setSurface(int surface) {
		this.surface = surface;
	}

	public String getDivisibilite() {
		return divisibilite;
	}

	public void setDivisibilite(String divisibilite) {
		this.divisibilite = divisibilite;
	}

	public String getDisponibilite() {
		return disponibilite;
	}

	public void setDisponibilite(String disponibilite) {
		this.disponibilite = disponibilite;
	}

	public String getTypeTransaction() {
		return typeTransaction;
	}

	public void setTypeTransaction(String typeTransaction) {
		this.typeTransaction = typeTransaction;
	}

	public String getTypeBien() {
		return typeBien;
	}

	public void setTypeBien(String typeBien) {
		this.typeBien = typeBien;
	}

	public String getLien() {
		return lien;
	}

	public void setLien(String lien) {
		this.lien = lien;
	}

	public String getLienPhoto() {
		return lienPhoto;
	}

	public void setLienPhoto(String lienPhoto) {
		this.lienPhoto = lienPhoto;
	}

	public String getContact() {
		return contact;
	}

	public void setContact(String contact) {
		this.contact = contact;
	}

	public String getSite() {
		return site;
	}

	public void setSite(String site) {
		this.site = site;
	}

	public String getReferenceSite() {
		return referenceSite;
	}

	public void setReferenceSite(String referenceSite) {
		this.referenceSite = referenceSite;
	}

	public String getIndicationPrix() {
		return indicationPrix;
	}

	public void setIndicationPrix(String indicationPrix) {
		this.indicationPrix = indicationPrix;
	}
}