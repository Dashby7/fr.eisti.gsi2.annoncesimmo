package fr.eisti.gsi2.mapper;

import java.util.List;

import org.mapstruct.Mapper;
import org.mapstruct.factory.Mappers;

import fr.eisti.gsi2.dto.Annonce;
import fr.eisti.gsi2.entities.AnnonceEntity;

@Mapper(componentModel = "spring")
public interface AnnonceMapper {
	
	AnnonceMapper INSTANCE = Mappers.getMapper(AnnonceMapper.class);
	
	public Annonce mapToDTO(AnnonceEntity annonceEntity);
	
	public AnnonceEntity mapToEntity(Annonce annonce);
	
	public List<Annonce> mapToDTO(List<AnnonceEntity> annonceEntity);
	
	public List<AnnonceEntity> mapToEntity(List<Annonce> annonce);
}
