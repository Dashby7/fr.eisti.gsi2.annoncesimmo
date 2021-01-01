CREATE TABLE `modifiee` (
  `nom_annonce` text,
  `ville` text,
  `adresse` text,
  `code_postal` text,
  `prix` text,
  `surface` bigint DEFAULT NULL,
  `divisibilite` text,
  `disponibilite` text,
  `type_transaction` text,
  `type_bien` text,
  `lien` text,
  `lien_photo` text,
  `contact` text,
  `site` text,
  `reference_du_site` text,
  `indication_prix` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;