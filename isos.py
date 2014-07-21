from util import hook

@hook.command
def isos(inp):
	"""isos <product> <version> [edition] <bits> [torrent] -- It will grab the correct ISO link for a download."""        

	dict = {'windows 7 pro 64': 'Windows 7 Pro 64-bit: http://msft.digitalrivercontent.net/win/X17-24281.iso'};
	dict['windows 7 home 64'] = "Windows 7 Home Premium 64-bit: http://msft.digitalrivercontent.net/win/X17-24209.iso";
	dict['windows 7 pro 32'] = "Windows 7 Pro 32-bit: http://msft.digitalrivercontent.net/win/X17-24280.iso";
	dict['windows 7 home 32'] = "Windows 7 Home Premium 32-bit: http://msft.digitalrivercontent.net/win/X17-24208.iso";
	dict['windows 7 ultimate 64'] = "Windows 7 Ultimate 64-bit: http://msft.digitalrivercontent.net/win/X17-24395.iso";
	dict['windows 7 ultimate 32'] = "Windows 7 Ultimate 32-bit: http://msft.digitalrivercontent.net/win/X17-24394.iso";
	dict['windows 8 pro 64'] = "Windows 8 Pro 64-bit: http://repo.comprepair.tk/Windows8_Pro/Windows8_Pro_ESD.iso | MD5: e4716c7086db4431a6fb1a8716df3d9f";
	dict['windows 8 pro 32'] = "Windows 8 Pro 32-bit: http://repo.comprepair.tk/Windows8_Pro/Windows8_Pro_ESD_x86.iso | MD5: 255eb2cfaca6cc398361033365f1eb28";
	dict['windows 8.1 pro 64'] = "Windows 8.1 Pro 64-bit: http://repo.comprepair.tk/Windows8.1_Pro/Windows_81_ESD_install_x64.iso | MD5: 5119bf941fdb96cbe839e9599186eda3";
	dict['windows 8.1 pro 32'] = "We do not have an ISO in the repository for that. Try using the official Microsoft downloader at http://goo.gl/qtfqo if you got a retail key.";
	dict['windows vista home 32'] = "Windows Vista Home Premium 32-bit: http://repo.comprepair.tk/WindowsVista_HomePremium/LRMCFRE_EN_DVD.iso | MD5: 1008f323d5170c8e614e52ccb85c0491";
	dict['windows vista home 64'] = "We do not have an ISO in the repository for that.";	
	dict['windows xp pro 32'] = "Windows XP Professional 32-bit: http://repo.comprepair.tk/WindowsXP_SP2_Professional/VX2POEM_EN.iso | MD5: 2d7f4e6e334e9a84c45231f5a40aa56f";
	dict['windows xp pro 64'] = "Windows XP Professional 64-bit (Uploaded by blumoon): http://repo.comprepair.tk/WindowsXP_SP2_Professional/CRMPXOEM_EN.ISO | SHA-1: da414d53d2ed40a7e6376d981203c49cc949ad24";
	dict['windows torrent'] = "Are you out of your mind? We don't recommend you use a Windows torrent under most circumstances.";
	
	items_windows = dict.keys()
	
	dict['ubuntu 14.04 64'] = "Ubuntu Desktop 14.04 (LTS) 64-bit: http://www.ubuntu.com/download/desktop/thank-you?country=US&version=14.04&architecture=amd64";
	dict['ubuntu 14.04 32'] = "Ubuntu Desktop 14.04 (LTS) 32-bit: http://www.ubuntu.com/download/desktop/thank-you?country=US&version=14.04&architecture=i386";
	dict['ubuntu 14.04 64 torrent'] = "magnet:?xt=urn:btih:4d753474429d817b80ff9e0c441ca660ec5d2450&dn=ubuntu-14.04-desktop-amd64.iso&tr=http%3A%2F%2Ftorrent.ubuntu.com%3A6969%2Fannounce&tr=http%3A%2F%2Fipv6.torrent.ubuntu.com%3A6969%2Fannounce";
	dict['ubuntu 14.04 32 torrent'] = "magnet:?xt=urn:btih:7a1073bc39e6b0b01e3730227b8ffea6aeac5d59&dn=ubuntu-14.04-desktop-i386.iso&tr=http%3A%2F%2Ftorrent.ubuntu.com%3A6969%2Fannounce&tr=http%3A%2F%2Fipv6.torrent.ubuntu.com%3A6969%2Fannounce";
	dict['mint 17 64'] = "Linux Mint 17 (Qiana) 64-bit: http://www.linuxmint.com/edition.php?id=158";
	dict['mint 17 32'] = "Linux Mint 17 (Qiana) 32-bit: http://www.linuxmint.com/edition.php?id=157";
	dict['mint 17 64 torrent'] = "magnet:?xt=urn:btih:bdc2d4a6f9dd39fc5996a460b6eaf5e2e4478894&dn=linuxmint-17-cinnamon-dvd-64bit.iso&tr=http%3A%2F%2Ftorrents.linuxmint.com%2Fannounce.php";
	dict['mint 17 32 torrent'] = "magnet:?xt=urn:btih:28123d060a2cd8598502f13ac6b720aebc6e0aad&dn=linuxmint-17-cinnamon-dvd-32bit.iso&tr=http%3A%2F%2Ftorrents.linuxmint.com%2Fannounce.php";
	dict['fedora 20 64'] = "Fedora Desktop 20 64-bit: http://download.fedoraproject.org/pub/fedora/linux/releases/20/Live/x86_64/Fedora-Live-Desktop-x86_64-20-1.iso";
	dict['fedora 20 32'] = "Fedora Desktop 20 32-bit: http://download.fedoraproject.org/pub/fedora/linux/releases/20/Live/i386/Fedora-Live-Desktop-i686-20-1.iso";
	dict['fedora 20 64 torrent'] = "magnet:?xt=urn:btih:724bcc8a53b854daa844e6bc204b95124a1074d6&dn=Fedora-20-x86%5F64-DVD&tr=http%3A%2F%2Ftorrent.fedoraproject.org%3A6969%2Fannounce";
	dict['fedora 20 32 torrent'] = "magnet:?xt=urn:btih:d6d123d9a9b108971ecb09ca6593d2593cd564a4&dn=Fedora-20-i386-DVD&tr=http%3A%2F%2Ftorrent.fedoraproject.org%3A6969%2Fannounce";
	dict['puppy 5.2.8 64'] = "Puppy Linux (Lucid) 5.2.8 Multi-Arch: http://distro.ibiblio.org/puppylinux/puppy-5.2.8/lupu-528.005.iso";
	dict['puppy 5.2.8 32'] = "Puppy Linux (Lucid) 5.2.8 Multi-Arch: http://distro.ibiblio.org/puppylinux/puppy-5.2.8/lupu-528.005.iso";
	dict['elementary luna 64'] = "Elementary OS Luna 64-bit: http://sourceforge.net/projects/elementaryos/files/stable/elementaryos-stable-amd64.20130810.iso/download";
	dict['elementary luna 32'] = "Elementary OS Luna 32-bit: http://sourceforge.net/projects/elementaryos/files/stable/elementaryos-stable-i386.20130810.iso/download";
	dict['elementary luna 64 torrent'] = "magnet:?xt=urn:btih:5c5978d6a76b960bb0504433ff6b408b183ebf38&dn=elementaryos-stable-amd64.20130810.iso&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&ws=http%3A%2F%2Fsuperb-sea2.dl.sourceforge.net%2Fproject%2Felementaryos%2Fstable%2Felementaryos-stable-amd64.20130810.iso&ws=http%3A%2F%2Fheanet.dl.sourceforge.net%2Fproject%2Felementaryos%2Fstable%2Felementaryos-stable-amd64.20130810.iso&ws=http%3A%2F%2Fignum.dl.sourceforge.net%2Fproject%2Felementaryos%2Fstable%2Felementaryos-stable-amd64.20130810.iso&ws=http%3A%2F%2Fcitylan.dl.sourceforge.net%2Fproject%2Felementaryos%2Fstable%2Felementaryos-stable-amd64.20130810.iso";
	dict['elementary luna 32 torrent'] = "magnet:?xt=urn:btih:455c7898a4f538887c7075e36e800e49f9940653&dn=elementaryos-stable-i386.20130810.iso&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&ws=http%3A%2F%2Fsuperb-sea2.dl.sourceforge.net%2Fproject%2Felementaryos%2Fstable%2Felementaryos-stable-i386.20130810.iso&ws=http%3A%2F%2Fheanet.dl.sourceforge.net%2Fproject%2Felementaryos%2Fstable%2Felementaryos-stable-i386.20130810.iso&ws=http%3A%2F%2Fignum.dl.sourceforge.net%2Fproject%2Felementaryos%2Fstable%2Felementaryos-stable-i386.20130810.iso&ws=http%3A%2F%2Fcitylan.dl.sourceforge.net%2Fproject%2Felementaryos%2Fstable%2Felementaryos-stable-i386.20130810.iso";
	dict['crunchbang 11 64'] = "Crunchbang Linux 11 (Waldorf) 64-bit: http://crunchbang.org/torrents/crunchbang-11-20130506-amd64.iso.torrent";
	dict['crunchbang 11 32'] = "Crunchbang Linux 11 (Wladorf) 32-bit: http://crunchbang.org/torrents/crunchbang-11-20130506-i686.iso.torrent";
	dict['crunchbang 11 64 torrent'] = "magnet:?xt=urn:btih:d9be6909325d28912f400fcb324005dd5861e49f&dn=crunchbang-11-20130506-amd64.iso&tr=http%3A%2F%2Fbttracker.crunchbanglinux.org%3A6969%2Fannounce";
	dict['crunchbang 11 32 torrent'] = "magnet:?xt=urn:btih:88fa8516ca2b3d3d4186752084f93a59918fa351&dn=crunchbang-11-20130506-i686.iso&tr=http%3A%2F%2Fbttracker.crunchbanglinux.org%3A6969%2Fannounce";
	dict['arch latest 64'] = "Arch Linux (Latest) 64-bit: https://www.archlinux.org/download/";
	dict['arch latest 32'] = "Arch Linux (Latest) 32-bit: https://www.archlinux.org/download/";
	dict['arch latest 64 torrent'] = "magnet:?xt=urn:btih:64b7700828fd44b37c0c045091939a2c0258ddc2&dn=archlinux-2014.06.01-dual.iso&tr=udp://tracker.archlinux.org:6969&tr=http://tracker.archlinux.org:6969/announce";
	dict['arch latest 32 torrent'] = "magnet:?xt=urn:btih:64b7700828fd44b37c0c045091939a2c0258ddc2&dn=archlinux-2014.06.01-dual.iso&tr=udp://tracker.archlinux.org:6969&tr=http://tracker.archlinux.org:6969/announce";
	dict['lubuntu 14.04 64'] = "Lubuntu Desktop 14.04 (LXDE) 64-bit: http://cdimage.ubuntu.com/lubuntu/releases/14.04/release/lubuntu-14.04-desktop-amd64.iso";
	dict['lubuntu 14.04 32'] = "Lubuntu Desktop 14.04 (LXDE) 32-bit: http://cdimage.ubuntu.com/lubuntu/releases/14.04/release/lubuntu-14.04-desktop-i386.iso";
	dict['lubuntu 14.04 64 torrent'] = "magnet:?xt=urn:btih:1ff46d3436df730b81ce36f9be7abb0a09971017&dn=lubuntu-14.04-desktop-amd64.iso&tr=http%3A%2F%2Ftorrent.ubuntu.com%3A6969%2Fannounce";
	dict['lubuntu 14.04 32 torrent'] = "magnet:?xt=urn:btih:ef21436f8b097cb76b7c488dd84f318e3d275a79&dn=lubuntu-14.04-desktop-i386.iso&tr=http%3A%2F%2Ftorrent.ubuntu.com%3A6969%2Fannounce";
	
	items = dict.keys()

	dict['dantheman'] = "Isn't he that guy who's username could be separated into dan the man?";
	dict['gduran144'] = "He clearly does not read the manuals.";
	dict['rod156'] = "No comment.";
	dict['mikee'] = "He is the big-boss, the owner, the top man.";
	dict['miss'] = "Hello!";
	dict['robotoverlordv2'] = "I guess he really wants to take over the world.";
	dict['robocop'] = "Have you looked at a mirror lately?";
	dict['noodlesdefyyou'] = "He works at Veeam, and worked at that evil company Comcast.";
	dict['eisenstein'] = "Some say he's not always a fan of bots.";
	dict['nurga'] = "He just appeared one day, how many people do you see doing that?";
	dict['bluemoon'] = "Does (s)he appear once in a blue moon?";
	dict['deliriumtremens'] = "He's a nice guy, and a good Python developer.";
	dict['phydeaux8635'] = "I got no idea what he does, but he does know iOS!";
	dict['torrinco'] = "He really wants an easter egg of himself.";
	dict['shadowhand'] = "Do the aforementioned deed, sodomite.";
	dict['aeo'] = "He does the #techsupport night shift.";
	dict['kumorigoe'] = "He knows Windows Deployment like the back of his hand!";
	dict['cyndro'] = "Cyndro or Cyndroid? You got me confused.";
	dict['thatoneroadie'] = "Well, he Snoonets and then Admins.";
	dict['thevaz'] = "He really wanted his own easter egg. I guess he is OK.";
	dict['afreshmelon'] = "aFreshMelon is 20, that is all you need to know.";
	
	
	inp = inp.lower()

	if inp == "print":
		print str(items)
		value = ', '.join(items)
		
	else:	
		if inp == "print windows":
			value = ', '.join(items_windows)
		else:
			value = dict.get(inp, "I could not find that ISO. You might want to check your syntax.");

	return value;
