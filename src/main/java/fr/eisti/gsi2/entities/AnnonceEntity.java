package fr.eisti.gsi2.entities;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity(name="annonce")
@Table(name="annonce")
public class AnnonceEntity implements Serializable {

	private static final long serialVersionUID = 2271314289867098430L;
	
	@Id
	@Column(name="id")
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	private Long id;
	
	@Column(name="nom_annonce")
	private String nomAnnonce;
	
	@Column(name="ville")
	private String ville;
	
	@Column(name="adresse")
	private String adresse;
	
	@Column(name="code_postal")
	private String codePostal;
	
	@Column(name="prix")
	private String prix;
	
	@Column(name="surface")
	private Long surface;
	
	@Column(name="divisibilite")
	private String divisibilite;
	
	@Column(name="disponibilite")
	private String disponibilite;
	
	@Column(name="type_transaction")
	private String typeTransaction;
	
	@Column(name="type_bien")
	private String typeBien;
	
	@Column(name="lien")
	private String lien;
	
	@Column(name="lien_photo")
	private String lienPhoto;
	
	@Column(name="contact")
	private String contact;
	
	@Column(name="site")
	private String site;
	
	@Column(name="reference_du_site")
	private String referenceSite;
	
	@Column(name="indication_prix")
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
	public String getPrix() {
		return prix;
	}
	public void setPrix(String prix) {
		this.prix = prix;
	}
	public Long getSurface() {
		return surface;
	}
	public void setSurface(Long surface) {
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