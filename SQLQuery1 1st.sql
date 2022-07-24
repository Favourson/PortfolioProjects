Select * 
From PortfolioProject1..CovidDeaths
where continent is not null
Order by 3,4

--Select * 
--From PortfolioProject1..CovidVaccinations
--Order by 3,4
--Select the data to be used

Select Location, date, total_cases, new_cases, total_deaths, population
From PortfolioProject1..CovidDeaths
where continent is not null
order by 1,2

-- Looking at total cases vs Total Deaths
-- Shows likelihood of dying if you contract covid in your country
Select Location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
From PortfolioProject1..CovidDeaths
where location like '%nigeria%'
order by 1,2


-- Looking at Total Cases vs Population
-- Shows what percentage of population got covid

Select Location, date, population, total_cases, (total_cases/population)*100 as PercentPopulationInfected
From PortfolioProject1..CovidDeaths
--where location like '%states%'
order by 1,2

-- Looking at countries with highest infection rate compared to population

Select Location, Population, Max(total_cases) as HihestInfectionCount, Max((total_cases/population))*100 as 
	PercentPopulationInfected
From PortfolioProject1..CovidDeaths
--where location like '%states%'
Group by Location, Population
order by PercentPopulationInfected desc

-- Showing the countries with highest death count per population

Select Location, MAX(cast(total_deaths as bigint)) as TotalDeathCount
From PortfolioProject1..CovidDeaths
--where location like '%states%'
where continent is not null
Group by Location
order by TotalDeathCount desc



-- LET"S BREAK THINGS DOWN BY CONTINENT


-- SHOWING THE CONTINENT WITH THE HIGHEST DEATH COUNT PER POPULATION

Select continent, MAX(cast(total_deaths as bigint)) as TotalDeathCount
From PortfolioProject1..CovidDeaths
--where location like '%states%'
where continent is not null
Group by continent
order by TotalDeathCount desc


-- GLOBAL NUMBERS
-- 1st GN total cases in the world and the total death and death percentage
Select SUM(new_cases) as total_cases, SUM(cast(new_deaths as bigint)) as total_deaths, SUM(cast(new_deaths as bigint))/SUM(new_cases)*100 as DeathPercentage
From PortfolioProject1..CovidDeaths
--where location like '%states%'
where continent is not null
--Group by date
order by 1,2

--2, GN is many stats of deatch and the date used to sort them based on global total figures

Select date, SUM(new_cases) as total_cases, SUM(cast(new_deaths as bigint)) as total_deaths, SUM(cast(new_deaths as bigint))/SUM(new_cases)*100 as DeathPercentage
From PortfolioProject1..CovidDeaths
--where location like '%states%'
where continent is not null
Group by date
order by 1,2


-- Looking at Total population vs vaccinations

Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(Convert(bigint, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location, dea.Date)
as RollingPeopleVaccinated,
--(RollingPeopleVaccinated/population)*100
From PortfolioProject1..CovidDeaths dea
Join PortfolioProject1..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null
order by 2,3


--USE CTE

With PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingPeopleVaccinated)
as
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(Convert(bigint, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location, dea.Date)
as RollingPeopleVaccinated
--(RollingPeopleVaccinated/population)*100
From PortfolioProject1..CovidDeaths dea
Join PortfolioProject1..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null
--order by 2,3
)
Select *, (RollingPeopleVaccinated/Population)*100
From PopvsVac



-- TEMP TABLE

DROP Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)


 
Insert into #PercentPopulationVaccinated
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(Convert(bigint, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location, dea.Date)
as RollingPeopleVaccinated
--(RollingPeopleVaccinated/population)*100
From PortfolioProject1..CovidDeaths dea
Join PortfolioProject1..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
--where dea.continent is not null
--order by 2,3

Select *, (RollingPeopleVaccinated/Population)*100
From #PercentPopulationVaccinated


-- CREATING VIEW TO STORE DATA FOR LATER VISUALIZATIONS


CREATE VIEW PercentPopulationVaccinated
as
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(Convert(bigint, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location, dea.Date)
as RollingPeopleVaccinated
--(RollingPeopleVaccinated/population)*100
From PortfolioProject1..CovidDeaths dea
Join PortfolioProject1..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null
--order by 2,3;

select *
from PercentPopulationVaccinated